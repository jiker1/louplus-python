"""init

Revision ID: ac3a305dcaec
Revises: 
Create Date: 2018-11-20 10:43:58.615038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac3a305dcaec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('cover', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('cover', sa.String(length=100), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_product',
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('shop_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_product')
    op.drop_table('favorite_product')
    op.drop_table('shop')
    op.drop_table('product')
    # ### end Alembic commands ###