import { ApeNode } from '@/types';
import { CaretRightOutlined } from '@ant-design/icons';
import { applyNodeChanges, NodeChange } from '@xyflow/react';
import { Collapse, Form, Select, Slider, theme } from 'antd';
import _ from 'lodash';
import { useCallback, useMemo } from 'react';
import { useIntl, useModel } from 'umi';
import { NodeInput } from './_node-input';
import { NodeOutputs } from './_outputs';
import { OutputParams } from './_outputs_params';
import { getCollapsePanelStyle } from './_styles';

export const ApeNodeVectorSearch = ({ node }: { node: ApeNode }) => {
  const { token } = theme.useToken();
  const { setNodes } = useModel('bots.$botId.flow.model');
  const { formatMessage } = useIntl();
  const { collections } = useModel('collection');

  const schema = useMemo(() => node.data.input.schema, [node]);
  const values = useMemo(() => node.data.input?.values || [], [node]);
  const applyChanges = useCallback(() => {
    setNodes((nds) => {
      const changes: NodeChange[] = [
        { id: node.id, type: 'replace', item: node },
      ];
      return applyNodeChanges(changes, nds) as ApeNode[];
    });
  }, [node]);

  return (
    <>
      <Collapse
        bordered={false}
        expandIcon={({ isActive }) => {
          return <CaretRightOutlined rotate={isActive ? 90 : 0} />;
        }}
        size="middle"
        defaultActiveKey={['1']}
        style={{ background: 'none' }}
        items={[
          {
            key: '1',
            label: formatMessage({ id: 'flow.input.params' }),
            style: getCollapsePanelStyle(token),
            children: (
              <>
                <Form layout="vertical" autoComplete="off">
                  <Form.Item
                    required
                    label={formatMessage({ id: 'collection.name' })}
                  >
                    <Select
                      variant="filled"
                      mode="multiple"
                      suffixIcon={null}
                      options={collections?.map((collection) => ({
                        label: collection.title,
                        value: collection.id,
                      }))}
                      value={_.get(values, 'collection_ids')}
                      onChange={(value) => {
                        _.set(values, 'collection_ids', value);
                        applyChanges();
                      }}
                      placeholder={formatMessage({ id: 'collection.select' })}
                    />
                  </Form.Item>
                  <Form.Item
                    label={formatMessage({ id: 'flow.top_k' })}
                    tooltip={formatMessage({ id: 'flow.top_k.tips' })}
                  >
                    <Slider
                      value={_.get(values, 'top_k')}
                      style={{ margin: 0 }}
                      min={_.get(schema, 'properties.top_k.minimum')}
                      max={_.get(schema, 'properties.top_k.maximum')}
                      step={1}
                      onChange={(value) => {
                        _.set(values, 'top_k', value);
                        applyChanges();
                      }}
                    />
                  </Form.Item>
                  <Form.Item
                    label={formatMessage({ id: 'flow.similarity_threshold' })}
                    tooltip={formatMessage({
                      id: 'flow.similarity_threshold.tips',
                    })}
                  >
                    <Slider
                      value={_.get(values, 'similarity_threshold')}
                      style={{ margin: 0 }}
                      min={_.get(
                        schema,
                        'properties.similarity_threshold.minimum',
                      )}
                      max={_.get(
                        schema,
                        'properties.similarity_threshold.maximum',
                      )}
                      step={0.01}
                      onChange={(value) => {
                        _.set(values, 'similarity_threshold', value);
                        applyChanges();
                      }}
                    />
                  </Form.Item>
                  <Form.Item
                    required
                    style={{ marginBottom: 0 }}
                    label={formatMessage({ id: 'flow.variable.global' })}
                  >
                    <NodeInput
                      value={_.get(values, 'query')}
                      disabled
                      onChange={(e) => {
                        _.set(values, 'query', e.currentTarget.value);
                        applyChanges();
                      }}
                      variant="filled"
                    />
                  </Form.Item>
                </Form>
              </>
            ),
          },
          {
            key: '2',
            label: formatMessage({ id: 'flow.output.params' }),
            style: getCollapsePanelStyle(token),
            children: <OutputParams node={node} />,
            extra: <NodeOutputs node={node} />,
          },
        ]}
      />
    </>
  );
};
