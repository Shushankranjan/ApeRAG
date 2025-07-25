/* tslint:disable */
/* eslint-disable */
/**
 * ApeRAG API
 * ApeRAG API Documentation
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


// May contain unused imports in some cases
// @ts-ignore
import type { TargetEntityDataRequest } from './target-entity-data-request';

/**
 * Request to merge multiple graph nodes directly using entity IDs. 
 * @export
 * @interface NodeMergeRequest
 */
export interface NodeMergeRequest {
    [key: string]: any;

    /**
     * List of entity IDs to merge directly
     * @type {Array<string>}
     * @memberof NodeMergeRequest
     */
    'entity_ids': Array<string>;
    /**
     * 
     * @type {TargetEntityDataRequest}
     * @memberof NodeMergeRequest
     */
    'target_entity_data'?: TargetEntityDataRequest;
}

