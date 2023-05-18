"""initial

Revision ID: 710ad76f34d5
Revises: 
Create Date: 2023-05-17 17:49:46.303875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '710ad76f34d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question_text', sa.String(), nullable=False),
    sa.Column('answer_text', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_id'), 'question', ['id'], unique=False)
    op.create_index(op.f('ix_question_question_id'), 'question', ['question_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_question_id'), table_name='question')
    op.drop_index(op.f('ix_question_id'), table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###