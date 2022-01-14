"""initial

Revision ID: 313aa36e86a8
Revises: 
Create Date: 2022-01-12 12:55:27.149581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313aa36e86a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shortened_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=255), nullable=True),
    sa.Column('short_link', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shortened_urls_short_link'), 'shortened_urls', ['short_link'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shortened_urls_short_link'), table_name='shortened_urls')
    op.drop_table('shortened_urls')
    # ### end Alembic commands ###
