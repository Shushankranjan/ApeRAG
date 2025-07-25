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
 * Node properties containing entity metadata
 * @export
 * @interface GraphNodeProperties
 */
export interface GraphNodeProperties {
    [key: string]: any;

    /**
     * Entity identifier
     * @type {string}
     * @memberof GraphNodeProperties
     */
    'entity_id'?: string;
    /**
     * Type of the entity
     * @type {string}
     * @memberof GraphNodeProperties
     */
    'entity_type'?: string;
    /**
     * Description of the entity
     * @type {string}
     * @memberof GraphNodeProperties
     */
    'description'?: string;
    /**
     * Source chunk ID where entity was extracted
     * @type {string}
     * @memberof GraphNodeProperties
     */
    'source_id'?: string;
    /**
     * Source file path
     * @type {string}
     * @memberof GraphNodeProperties
     */
    'file_path'?: string;
    /**
     * Creation timestamp
     * @type {number}
     * @memberof GraphNodeProperties
     */
    'created_at'?: number;
}

