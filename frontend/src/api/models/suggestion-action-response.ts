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
import type { NodeMergeResponse } from './node-merge-response';

/**
 * Response containing suggestion action results
 * @export
 * @interface SuggestionActionResponse
 */
export interface SuggestionActionResponse {
    /**
     * Status of the action operation
     * @type {string}
     * @memberof SuggestionActionResponse
     */
    'status': SuggestionActionResponseStatusEnum;
    /**
     * Detailed message about the action operation
     * @type {string}
     * @memberof SuggestionActionResponse
     */
    'message': string;
    /**
     * The suggestion ID that was processed
     * @type {string}
     * @memberof SuggestionActionResponse
     */
    'suggestion_id': string;
    /**
     * The action that was performed (normalized to lowercase)
     * @type {string}
     * @memberof SuggestionActionResponse
     */
    'action': SuggestionActionResponseActionEnum;
    /**
     * Merge operation result (only present when action is \'accept\')
     * @type {NodeMergeResponse}
     * @memberof SuggestionActionResponse
     */
    'merge_result'?: NodeMergeResponse;
}

export const SuggestionActionResponseStatusEnum = {
    success: 'success',
    error: 'error'
} as const;

export type SuggestionActionResponseStatusEnum = typeof SuggestionActionResponseStatusEnum[keyof typeof SuggestionActionResponseStatusEnum];
export const SuggestionActionResponseActionEnum = {
    accept: 'accept',
    reject: 'reject'
} as const;

export type SuggestionActionResponseActionEnum = typeof SuggestionActionResponseActionEnum[keyof typeof SuggestionActionResponseActionEnum];


