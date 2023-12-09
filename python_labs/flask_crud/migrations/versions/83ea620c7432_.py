"""empty message

Revision ID: 83ea620c7432
Revises: 
Create Date: 2023-12-10 01:40:02.603821

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '83ea620c7432'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app_student', schema=None) as batch_op:
        batch_op.drop_index('firstname')
        batch_op.drop_index('lastname')
        batch_op.drop_index('patronymic')

    op.drop_table('app_student')
    with op.batch_alter_table('app_university', schema=None) as batch_op:
        batch_op.drop_index('name')
        batch_op.drop_index('short_name')

    op.drop_table('app_university')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_university',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('short_name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('create_date', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('app_university', schema=None) as batch_op:
        batch_op.create_index('short_name', ['short_name'], unique=False)
        batch_op.create_index('name', ['name'], unique=False)

    op.create_table('app_student',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('firstname', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('lastname', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('patronymic', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('birthdate', sa.DATE(), nullable=False),
    sa.Column('entrance_date', sa.DATE(), nullable=False),
    sa.Column('university_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['university_id'], ['app_university.id'], name='app_student_university_id_2dbd3f2f_fk_app_university_id'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('app_student', schema=None) as batch_op:
        batch_op.create_index('patronymic', ['patronymic'], unique=False)
        batch_op.create_index('lastname', ['lastname'], unique=False)
        batch_op.create_index('firstname', ['firstname'], unique=False)

    # ### end Alembic commands ###
