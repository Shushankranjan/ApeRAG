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
 * Request to take action on a merge suggestion
 * @export
 * @interface SuggestionActionRequest
 */
export interface SuggestionActionRequest {
    [key: string]: any;

    /**
     * Action to take on the suggestion (case-insensitive, e.g., \'Accept\', \'REJECT\', \'accept\')
     * @type {string}
     * @memberof SuggestionActionRequest
     */
    'action': SuggestionActionRequestActionEnum;
    /**
     * Optional override for target entity data (only used when action is \'accept\')
     * @type {TargetEntityDataRequest}
     * @memberof SuggestionActionRequest
     */
    'target_entity_data'?: TargetEntityDataRequest;
}

export const SuggestionActionRequestActionEnum = {
    accept: 'accept',
    reject: 'reject'
} as const;

export type SuggestionActionRequestActionEnum = typeof SuggestionActionRequestActionEnum[keyof typeof SuggestionActionRequestActionEnum];


