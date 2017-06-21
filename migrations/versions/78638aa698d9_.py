"""empty message

Revision ID: 78638aa698d9
Revises: 
Create Date: 2017-06-06 23:38:12.483376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78638aa698d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('centrals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_UUID', sa.String(length=20), nullable=False),
    sa.Column('locationName', sa.String(length=20), nullable=False),
    sa.Column('xCoord', sa.Integer(), nullable=False),
    sa.Column('yCoord', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_centrals_locationName'), 'centrals', ['locationName'], unique=False)
    op.create_index(op.f('ix_centrals_xCoord'), 'centrals', ['xCoord'], unique=False)
    op.create_index(op.f('ix_centrals_yCoord'), 'centrals', ['yCoord'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('firstName', sa.String(length=100), nullable=True),
    sa.Column('lastName', sa.String(length=100), nullable=True),
    sa.Column('registered', sa.DateTime(), nullable=False),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_admin'), 'users', ['admin'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.create_table('peripherals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_UUID', sa.String(length=20), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('peripherals')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_admin'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_centrals_yCoord'), table_name='centrals')
    op.drop_index(op.f('ix_centrals_xCoord'), table_name='centrals')
    op.drop_index(op.f('ix_centrals_locationName'), table_name='centrals')
    op.drop_table('centrals')
    # ### end Alembic commands ###