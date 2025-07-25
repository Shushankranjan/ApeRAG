# Copyright 2025 ApeCloud, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from threading import Lock

from aperag.db.models import APIType
from aperag.db.ops import db_ops
from aperag.llm.completion.completion_service import CompletionService
from aperag.llm.llm_error_types import (
    CompletionError,
    InvalidConfigurationError,
    ModelNotFoundError,
    ProviderNotFoundError,
)
from aperag.schema.utils import parseCollectionConfig

logger = logging.getLogger(__name__)

mutex = Lock()


def synchronized(func):
    def wrapper(*args, **kwargs):
        with mutex:
            return func(*args, **kwargs)

    return wrapper


@synchronized
def _get_completion_service(
    completion_provider: str,
    completion_model: str,
    completion_service_url: str,
    completion_service_api_key: str,
    temperature: float = 0.1,
    max_tokens: int = None,
    vision: bool = False,
) -> CompletionService:
    """
    Create and configure a completion service instance.

    Args:
        completion_provider: The completion provider name
        completion_model: The completion model name
        completion_service_url: The API base URL
        completion_service_api_key: The API key
        temperature: Temperature for completion
        max_tokens: Maximum tokens for completion

    Returns:
        CompletionService instance

    Raises:
        CompletionError: If service creation fails
    """
    try:
        completion_svc = CompletionService(
            provider=completion_provider,
            model=completion_model,
            base_url=completion_service_url,
            api_key=completion_service_api_key,
            temperature=temperature,
            max_tokens=max_tokens,
            vision=vision,
        )
        return completion_svc
    except CompletionError:
        # Re-raise completion errors
        raise
    except Exception as e:
        logger.error(f"Failed to create completion model {completion_provider}/{completion_model}: {str(e)}")
        raise CompletionError(
            f"Failed to create completion model: {str(e)}",
            {"provider": completion_provider, "model": completion_model, "api_base": completion_service_url},
        ) from e


def get_collection_completion_service_sync(collection) -> CompletionService:
    """
    Get completion service for a collection synchronously.

    Args:
        collection: The collection object with configuration

    Returns:
        CompletionService instance

    Raises:
        ProviderNotFoundError: If the completion provider is not found
        ModelNotFoundError: If the completion model is not found
        InvalidConfigurationError: If configuration is invalid
        CompletionError: If completion service creation fails
    """
    try:
        config = parseCollectionConfig(collection.config)
    except Exception as e:
        logger.error(f"Failed to parse collection config: {str(e)}")
        raise InvalidConfigurationError(
            "collection.config", collection.config, f"Invalid collection configuration: {str(e)}"
        ) from e

    completion_msp = config.completion.model_service_provider
    completion_model_name = config.completion.model
    custom_llm_provider = config.completion.custom_llm_provider
    temperature = config.completion.temperature or 0.1

    logger.info("get_collection_completion_service_sync %s %s", completion_msp, completion_model_name)

    # Validate configuration fields
    if not completion_msp:
        raise InvalidConfigurationError(
            "completion.model_service_provider", completion_msp, "Model service provider cannot be empty"
        )

    if not completion_model_name:
        raise InvalidConfigurationError("completion.model", completion_model_name, "Model name cannot be empty")

    if not custom_llm_provider:
        raise InvalidConfigurationError(
            "completion.custom_llm_provider", custom_llm_provider, "Custom LLM provider cannot be empty"
        )

    completion_service_api_key = db_ops.query_provider_api_key(completion_msp, collection.user)
    if not completion_service_api_key:
        raise InvalidConfigurationError("api_key", None, f"API KEY not found for LLM Provider: {completion_msp}")

    try:
        llm_provider = db_ops.query_llm_provider_by_name(completion_msp)
        if not llm_provider:
            raise ModelNotFoundError(completion_model_name, completion_msp, "Completion")
        completion_service_url = llm_provider.base_url
    except Exception as e:
        logger.error(f"Failed to query LLM provider '{completion_msp}': {str(e)}")
        raise ProviderNotFoundError(completion_msp, "Completion") from e

    if not completion_service_url:
        raise InvalidConfigurationError(
            "base_url", completion_service_url, f"Base URL not configured for provider '{completion_msp}'"
        )

    logger.info("get_collection_completion_service %s", completion_service_url)

    try:
        is_vision_model = False
        model_info = db_ops.query_llm_provider_model(completion_msp, APIType.COMPLETION.value, completion_model_name)
        if model_info:
            is_vision_model = model_info.has_tag("vision")
    except Exception as e:
        logger.error(f"Failed to query LLM provider model '{completion_model_name}': {str(e)}")
        raise

    try:
        return _get_completion_service(
            completion_provider=custom_llm_provider,
            completion_model=completion_model_name,
            completion_service_url=completion_service_url,
            completion_service_api_key=completion_service_api_key,
            temperature=temperature,
            vision=is_vision_model,
        )
    except CompletionError:
        # Re-raise completion errors
        raise
    except Exception as e:
        logger.error(f"Failed to get completion service for collection: {str(e)}")
        raise CompletionError(
            f"Failed to get completion service for collection: {str(e)}",
            {
                "collection_id": getattr(collection, "id", "unknown"),
                "provider": completion_msp,
                "model": completion_model_name,
            },
        ) from e
