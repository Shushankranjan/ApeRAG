"""empty message

Revision ID: 8e8b89db412c
Revises: b3a2c218442f
Create Date: 2025-07-22 18:17:09.719803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e8b89db412c'
down_revision: Union[str, None] = 'b3a2c218442f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('api_key', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('audit_log', 'resource_type',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_comment='Resource type',
               existing_nullable=True)
    op.alter_column('bot', 'type',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('bot', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('chat', 'peer_type',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('chat', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('collection', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('collection', 'type',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('collection_summary', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('document', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('document_index', 'index_type',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('document_index', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('graph_index_merge_suggestions', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('invitation', 'role',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('llm_provider_models', 'api',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('message_feedback', 'type',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=True)
    op.alter_column('message_feedback', 'tag',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=True)
    op.alter_column('message_feedback', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=True)
    op.alter_column('model_service_provider', 'status',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('user', 'role',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'role',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('model_service_provider', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('message_feedback', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=True)
    op.alter_column('message_feedback', 'tag',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=True)
    op.alter_column('message_feedback', 'type',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=True)
    op.alter_column('llm_provider_models', 'api',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('invitation', 'role',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('graph_index_merge_suggestions', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('document_index', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('document_index', 'index_type',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('document', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('collection_summary', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('collection', 'type',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('collection', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('chat', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('chat', 'peer_type',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('bot', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('bot', 'type',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('audit_log', 'resource_type',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_comment='Resource type',
               existing_nullable=True)
    op.alter_column('api_key', 'status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    # ### end Alembic commands ###
