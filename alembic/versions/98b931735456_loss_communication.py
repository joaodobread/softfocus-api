"""loss_communication

Revision ID: 98b931735456
Revises: ed1beefbcbd8
Create Date: 2022-05-04 01:06:36.218715

"""
from datetime import datetime
from email.policy import default
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as g2

# revision identifiers, used by Alembic.
revision = '98b931735456'
down_revision = 'ed1beefbcbd8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'loss_communication',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('analysts_id', sa.Integer, nullable=False),
        sa.Column('farmer_name', sa.String(300), nullable=False),
        sa.Column('farmer_email', sa.String(300), nullable=False),
        sa.Column('farmer_document', sa.String(20), nullable=False),
        sa.Column('location', g2.Geometry(
            geometry_type='POINT', srid=4326), nullable=False),
        sa.Column('harvest_date', sa.DateTime, nullable=False),
        sa.Column('couse_of_loss', sa.Enum('excessive_rain', 'frost',
                  'hail', 'dry', 'gale', 'ray', name='couse_of_loss_enum'), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow),
        sa.Column('deleted', sa.Boolean, default=False, nullable=True),
        sa.ForeignKeyConstraint(['analysts_id'], ['analysts.id'])
    )


def downgrade():
    op.drop_table('loss_communication')
