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



/**
 * Edge properties containing relationship metadata
 * @export
 * @interface GraphEdgeProperties
 */
export interface GraphEdgeProperties {
    [key: string]: any;

    /**
     * Relationship weight/strength
     * @type {number}
     * @memberof GraphEdgeProperties
     */
    'weight'?: number;
    /**
     * Description of the relationship
     * @type {string}
     * @memberof GraphEdgeProperties
     */
    'description'?: string;
    /**
     * Keywords associated with the relationship
     * @type {string}
     * @memberof GraphEdgeProperties
     */
    'keywords'?: string;
    /**
     * Source chunk ID where relationship was extracted
     * @type {string}
     * @memberof GraphEdgeProperties
     */
    'source_id'?: string;
    /**
     * Source file path
     * @type {string}
     * @memberof GraphEdgeProperties
     */
    'file_path'?: string;
    /**
     * Creation timestamp
     * @type {number}
     * @memberof GraphEdgeProperties
     */
    'created_at'?: number;
}

