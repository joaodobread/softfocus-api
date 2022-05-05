"""init

Revision ID: ed1beefbcbd8
Revises:
Create Date: 2022-05-03 21:53:19.901956

"""
from datetime import datetime
import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg


# revision identifiers, used by Alembic.
revision = 'ed1beefbcbd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'analysts',
        sa.Column('id', pg.UUID(as_uuid=True),
                  primary_key=True, default=uuid.uuid4),
        sa.Column('name', sa.String(300), nullable=False),
        sa.Column('email', sa.String(300), nullable=False, unique=True),
        sa.Column('password', sa.String(300), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False,
                  default=datetime.utcnow()),
        sa.Column('is_super', sa.Boolean, nullable=False, default=0),
    )


def downgrade():
    op.drop_table('analysts')
