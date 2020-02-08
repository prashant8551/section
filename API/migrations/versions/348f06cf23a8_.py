"""empty message

Revision ID: 348f06cf23a8
Revises: 
Create Date: 2020-02-08 01:09:49.552680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '348f06cf23a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('role_title', sa.String(length=255), nullable=False),
    sa.Column('role_description', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('sections',
    sa.Column('section_id', sa.Integer(), nullable=False),
    sa.Column('section_title', sa.String(length=255), nullable=False),
    sa.Column('section_description', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('section_id')
    )
    op.create_table('operations',
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.Column('section_id', sa.Integer(), nullable=True),
    sa.Column('operation_title', sa.String(length=255), nullable=False),
    sa.Column('operation_description', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['section_id'], ['sections.section_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('operation_id')
    )
    op.create_table('roleconfig',
    sa.Column('role_config_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('operation_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['operation_id'], ['operations.operation_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('role_config_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roleconfig')
    op.drop_table('operations')
    op.drop_table('sections')
    op.drop_table('roles')
    # ### end Alembic commands ###