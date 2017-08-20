"""empty message

Revision ID: 6b0266976763
Revises: None
Create Date: 2017-08-20 07:24:07.866697

"""

# revision identifiers, used by Alembic.
revision = '6b0266976763'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=35), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('is_author', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('admin', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('slug', sa.String(length=256), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('live', sa.Boolean(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.drop_table('procs_priv')
    op.drop_table('time_zone_transition_type')
    op.drop_table('slow_log')
    op.drop_table('time_zone_name')
    op.drop_table('event')
    op.drop_table('proc')
    op.drop_table('columns_priv')
    op.drop_table('servers')
    op.drop_table('help_keyword')
    op.drop_table('roles_mapping')
    op.drop_table('column_stats')
    op.drop_table('time_zone_leap_second')
    op.drop_table('innodb_index_stats')
    op.drop_table('table_stats')
    op.drop_table('user')
    op.drop_table('help_topic')
    op.drop_table('time_zone')
    op.drop_table('time_zone_transition')
    op.drop_table('func')
    op.drop_table('general_log')
    op.drop_table('help_relation')
    op.drop_table('host')
    op.drop_table('plugin')
    op.drop_table('proxies_priv')
    op.drop_table('tables_priv')
    op.drop_table('index_stats')
    op.drop_table('innodb_table_stats')
    op.drop_table('help_category')
    op.drop_table('gtid_slave_pos')
    op.drop_table('db')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Db', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('User', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Select_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Insert_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Update_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Delete_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Drop_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Grant_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('References_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Index_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Alter_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_tmp_table_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Lock_tables_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_view_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Show_view_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_routine_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Alter_routine_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Execute_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Event_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Trigger_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.PrimaryKeyConstraint('Host', 'Db', 'User'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Database privileges',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('gtid_slave_pos',
    sa.Column('domain_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('sub_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('server_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('seq_no', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('domain_id', 'sub_id'),
    mysql_comment=u'Replication slave GTID position',
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('help_category',
    sa.Column('help_category_id', mysql.SMALLINT(display_width=5, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('name', mysql.CHAR(length=64), nullable=False),
    sa.Column('parent_category_id', mysql.SMALLINT(display_width=5, unsigned=True), autoincrement=False, nullable=True),
    sa.Column('url', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('help_category_id'),
    mysql_comment=u'help categories',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('innodb_table_stats',
    sa.Column('database_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('table_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('last_update', mysql.TIMESTAMP(), nullable=False),
    sa.Column('n_rows', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('clustered_index_size', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('sum_of_other_index_sizes', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('database_name', 'table_name'),
    mysql_collate=u'utf8_bin',
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('index_stats',
    sa.Column('db_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('table_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('index_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('prefix_arity', mysql.INTEGER(display_width=11, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('avg_frequency', mysql.DECIMAL(precision=12, scale=4), nullable=True),
    sa.PrimaryKeyConstraint('db_name', 'table_name', 'index_name', 'prefix_arity'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Statistics on Indexes',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('tables_priv',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Db', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('User', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Table_name', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Grantor', mysql.CHAR(collation=u'utf8_bin', length=141), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Timestamp', mysql.TIMESTAMP(), nullable=False),
    sa.Column('Table_priv', mysql.SET(charset=u'utf8', length=11), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Column_priv', mysql.SET(charset=u'utf8', length=10), server_default=sa.text(u"''"), nullable=False),
    sa.PrimaryKeyConstraint('Host', 'Db', 'User', 'Table_name'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Table privileges',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('proxies_priv',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('User', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Proxied_host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Proxied_user', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('With_grant', mysql.TINYINT(display_width=1), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('Grantor', mysql.CHAR(collation=u'utf8_bin', length=141), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Timestamp', mysql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('Host', 'User', 'Proxied_host', 'Proxied_user'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'User proxy privileges',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('plugin',
    sa.Column('name', mysql.VARCHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('dl', mysql.VARCHAR(length=128), server_default=sa.text(u"''"), nullable=False),
    sa.PrimaryKeyConstraint('name'),
    mysql_comment=u'MySQL plugins',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('host',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Db', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Select_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Insert_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Update_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Delete_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Drop_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Grant_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('References_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Index_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Alter_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_tmp_table_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Lock_tables_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_view_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Show_view_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_routine_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Alter_routine_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Execute_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Trigger_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.PrimaryKeyConstraint('Host', 'Db'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Host privileges;  Merged with database privileges',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('help_relation',
    sa.Column('help_topic_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('help_keyword_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('help_keyword_id', 'help_topic_id'),
    mysql_comment=u'keyword-topic relation',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('general_log',
    sa.Column('event_time', mysql.TIMESTAMP(fsp=6), nullable=False),
    sa.Column('user_host', mysql.MEDIUMTEXT(), nullable=False),
    sa.Column('thread_id', mysql.BIGINT(display_width=21, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('server_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('command_type', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('argument', mysql.MEDIUMTEXT(), nullable=False),
    mysql_comment=u'General log',
    mysql_default_charset=u'utf8',
    mysql_engine=u'CSV'
    )
    op.create_table('func',
    sa.Column('name', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('ret', mysql.TINYINT(display_width=1), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('dl', mysql.CHAR(collation=u'utf8_bin', length=128), server_default=sa.text(u"''"), nullable=False),
    sa.Column('type', mysql.ENUM(u'function', u'aggregate', charset=u'utf8'), nullable=False),
    sa.PrimaryKeyConstraint('name'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'User defined functions',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('time_zone_transition',
    sa.Column('Time_zone_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('Transition_time', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('Transition_type_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('Time_zone_id', 'Transition_time'),
    mysql_comment=u'Time zone transitions',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('time_zone',
    sa.Column('Time_zone_id', mysql.INTEGER(display_width=10, unsigned=True), nullable=False),
    sa.Column('Use_leap_seconds', mysql.ENUM(u'Y', u'N'), server_default=sa.text(u"'N'"), nullable=False),
    sa.PrimaryKeyConstraint('Time_zone_id'),
    mysql_comment=u'Time zones',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('help_topic',
    sa.Column('help_topic_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('name', mysql.CHAR(length=64), nullable=False),
    sa.Column('help_category_id', mysql.SMALLINT(display_width=5, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=False),
    sa.Column('example', mysql.TEXT(), nullable=False),
    sa.Column('url', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('help_topic_id'),
    mysql_comment=u'help topics',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('user',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('User', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Password', mysql.CHAR(charset=u'latin1', collation=u'latin1_bin', length=41), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Select_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Insert_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Update_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Delete_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Drop_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Reload_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Shutdown_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Process_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('File_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Grant_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('References_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Index_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Alter_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Show_db_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Super_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_tmp_table_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Lock_tables_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Execute_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Repl_slave_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Repl_client_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_view_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Show_view_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_routine_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Alter_routine_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_user_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Event_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Trigger_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('Create_tablespace_priv', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('ssl_type', mysql.ENUM(u'', u'ANY', u'X509', u'SPECIFIED', charset=u'utf8'), server_default=sa.text(u"''"), nullable=False),
    sa.Column('ssl_cipher', sa.BLOB(), nullable=False),
    sa.Column('x509_issuer', sa.BLOB(), nullable=False),
    sa.Column('x509_subject', sa.BLOB(), nullable=False),
    sa.Column('max_questions', mysql.INTEGER(display_width=11, unsigned=True), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('max_updates', mysql.INTEGER(display_width=11, unsigned=True), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('max_connections', mysql.INTEGER(display_width=11, unsigned=True), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('max_user_connections', mysql.INTEGER(display_width=11), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('plugin', mysql.CHAR(charset=u'latin1', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('authentication_string', mysql.TEXT(collation=u'utf8_bin'), nullable=False),
    sa.Column('password_expired', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('is_role', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    sa.Column('default_role', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('max_statement_time', mysql.DECIMAL(precision=12, scale=6), nullable=False),
    sa.PrimaryKeyConstraint('Host', 'User'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Users and global privileges',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('table_stats',
    sa.Column('db_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('table_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('cardinality', mysql.BIGINT(display_width=21, unsigned=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('db_name', 'table_name'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Statistics on Tables',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('innodb_index_stats',
    sa.Column('database_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('table_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('index_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('last_update', mysql.TIMESTAMP(), nullable=False),
    sa.Column('stat_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('stat_value', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('sample_size', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=True),
    sa.Column('stat_description', mysql.VARCHAR(collation=u'utf8_bin', length=1024), nullable=False),
    sa.PrimaryKeyConstraint('database_name', 'table_name', 'index_name', 'stat_name'),
    mysql_collate=u'utf8_bin',
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('time_zone_leap_second',
    sa.Column('Transition_time', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('Correction', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('Transition_time'),
    mysql_comment=u'Leap seconds information for time zones',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('column_stats',
    sa.Column('db_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('table_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('column_name', mysql.VARCHAR(collation=u'utf8_bin', length=64), nullable=False),
    sa.Column('min_value', sa.VARBINARY(length=255), nullable=True),
    sa.Column('max_value', sa.VARBINARY(length=255), nullable=True),
    sa.Column('nulls_ratio', mysql.DECIMAL(precision=12, scale=4), nullable=True),
    sa.Column('avg_length', mysql.DECIMAL(precision=12, scale=4), nullable=True),
    sa.Column('avg_frequency', mysql.DECIMAL(precision=12, scale=4), nullable=True),
    sa.Column('hist_size', mysql.TINYINT(display_width=3, unsigned=True), autoincrement=False, nullable=True),
    sa.Column('hist_type', mysql.ENUM(u'SINGLE_PREC_HB', u'DOUBLE_PREC_HB', collation=u'utf8_bin'), nullable=True),
    sa.Column('histogram', sa.VARBINARY(length=255), nullable=True),
    sa.PrimaryKeyConstraint('db_name', 'table_name', 'column_name'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Statistics on Columns',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('roles_mapping',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('User', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Role', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Admin_option', mysql.ENUM(u'N', u'Y', charset=u'utf8'), server_default=sa.text(u"'N'"), nullable=False),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Granted roles',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('help_keyword',
    sa.Column('help_keyword_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('name', mysql.CHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('help_keyword_id'),
    mysql_comment=u'help keywords',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('servers',
    sa.Column('Server_name', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Host', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Db', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Username', mysql.CHAR(length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Password', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Port', mysql.INTEGER(display_width=4), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('Socket', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Wrapper', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Owner', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.PrimaryKeyConstraint('Server_name'),
    mysql_comment=u'MySQL Foreign Servers table',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('columns_priv',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Db', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('User', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Table_name', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Column_name', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Timestamp', mysql.TIMESTAMP(), nullable=False),
    sa.Column('Column_priv', mysql.SET(charset=u'utf8', length=10), server_default=sa.text(u"''"), nullable=False),
    sa.PrimaryKeyConstraint('Host', 'Db', 'User', 'Table_name', 'Column_name'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Column privileges',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('proc',
    sa.Column('db', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('name', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('type', mysql.ENUM(u'FUNCTION', u'PROCEDURE'), nullable=False),
    sa.Column('specific_name', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('language', mysql.ENUM(u'SQL'), server_default=sa.text(u"'SQL'"), nullable=False),
    sa.Column('sql_data_access', mysql.ENUM(u'CONTAINS_SQL', u'NO_SQL', u'READS_SQL_DATA', u'MODIFIES_SQL_DATA'), server_default=sa.text(u"'CONTAINS_SQL'"), nullable=False),
    sa.Column('is_deterministic', mysql.ENUM(u'YES', u'NO'), server_default=sa.text(u"'NO'"), nullable=False),
    sa.Column('security_type', mysql.ENUM(u'INVOKER', u'DEFINER'), server_default=sa.text(u"'DEFINER'"), nullable=False),
    sa.Column('param_list', sa.BLOB(), nullable=False),
    sa.Column('returns', mysql.LONGBLOB(), nullable=False),
    sa.Column('body', mysql.LONGBLOB(), nullable=False),
    sa.Column('definer', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=141), server_default=sa.text(u"''"), nullable=False),
    sa.Column('created', mysql.TIMESTAMP(), nullable=False),
    sa.Column('modified', mysql.TIMESTAMP(), server_default=sa.text(u"'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('sql_mode', mysql.SET(length=26), server_default=sa.text(u"''"), nullable=False),
    sa.Column('comment', mysql.TEXT(charset=u'utf8', collation=u'utf8_bin'), nullable=False),
    sa.Column('character_set_client', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=32), nullable=True),
    sa.Column('collation_connection', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=32), nullable=True),
    sa.Column('db_collation', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=32), nullable=True),
    sa.Column('body_utf8', mysql.LONGBLOB(), nullable=True),
    sa.PrimaryKeyConstraint('db', 'name', 'type'),
    mysql_comment=u'Stored Procedures',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('event',
    sa.Column('db', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('name', mysql.CHAR(length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('body', mysql.LONGBLOB(), nullable=False),
    sa.Column('definer', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=141), server_default=sa.text(u"''"), nullable=False),
    sa.Column('execute_at', mysql.DATETIME(), nullable=True),
    sa.Column('interval_value', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('interval_field', mysql.ENUM(u'YEAR', u'QUARTER', u'MONTH', u'DAY', u'HOUR', u'MINUTE', u'WEEK', u'SECOND', u'MICROSECOND', u'YEAR_MONTH', u'DAY_HOUR', u'DAY_MINUTE', u'DAY_SECOND', u'HOUR_MINUTE', u'HOUR_SECOND', u'MINUTE_SECOND', u'DAY_MICROSECOND', u'HOUR_MICROSECOND', u'MINUTE_MICROSECOND', u'SECOND_MICROSECOND'), nullable=True),
    sa.Column('created', mysql.TIMESTAMP(), nullable=False),
    sa.Column('modified', mysql.TIMESTAMP(), server_default=sa.text(u"'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('last_executed', mysql.DATETIME(), nullable=True),
    sa.Column('starts', mysql.DATETIME(), nullable=True),
    sa.Column('ends', mysql.DATETIME(), nullable=True),
    sa.Column('status', mysql.ENUM(u'ENABLED', u'DISABLED', u'SLAVESIDE_DISABLED'), server_default=sa.text(u"'ENABLED'"), nullable=False),
    sa.Column('on_completion', mysql.ENUM(u'DROP', u'PRESERVE'), server_default=sa.text(u"'DROP'"), nullable=False),
    sa.Column('sql_mode', mysql.SET(length=26), server_default=sa.text(u"''"), nullable=False),
    sa.Column('comment', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('originator', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('time_zone', mysql.CHAR(charset=u'latin1', length=64), server_default=sa.text(u"'SYSTEM'"), nullable=False),
    sa.Column('character_set_client', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=32), nullable=True),
    sa.Column('collation_connection', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=32), nullable=True),
    sa.Column('db_collation', mysql.CHAR(charset=u'utf8', collation=u'utf8_bin', length=32), nullable=True),
    sa.Column('body_utf8', mysql.LONGBLOB(), nullable=True),
    sa.PrimaryKeyConstraint('db', 'name'),
    mysql_comment=u'Events',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('time_zone_name',
    sa.Column('Name', mysql.CHAR(length=64), nullable=False),
    sa.Column('Time_zone_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('Name'),
    mysql_comment=u'Time zone names',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('slow_log',
    sa.Column('start_time', mysql.TIMESTAMP(fsp=6), nullable=False),
    sa.Column('user_host', mysql.MEDIUMTEXT(), nullable=False),
    sa.Column('query_time', mysql.TIME(fsp=6), nullable=False),
    sa.Column('lock_time', mysql.TIME(fsp=6), nullable=False),
    sa.Column('rows_sent', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('rows_examined', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('db', mysql.VARCHAR(length=512), nullable=False),
    sa.Column('last_insert_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('insert_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('server_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('sql_text', mysql.MEDIUMTEXT(), nullable=False),
    sa.Column('thread_id', mysql.BIGINT(display_width=21, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('rows_affected', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    mysql_comment=u'Slow log',
    mysql_default_charset=u'utf8',
    mysql_engine=u'CSV'
    )
    op.create_table('time_zone_transition_type',
    sa.Column('Time_zone_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('Transition_type_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('Offset', mysql.INTEGER(display_width=11), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('Is_DST', mysql.TINYINT(display_width=3, unsigned=True), server_default=sa.text(u'0'), autoincrement=False, nullable=False),
    sa.Column('Abbreviation', mysql.CHAR(length=8), server_default=sa.text(u"''"), nullable=False),
    sa.PrimaryKeyConstraint('Time_zone_id', 'Transition_type_id'),
    mysql_comment=u'Time zone transition types',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.create_table('procs_priv',
    sa.Column('Host', mysql.CHAR(collation=u'utf8_bin', length=60), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Db', mysql.CHAR(collation=u'utf8_bin', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('User', mysql.CHAR(collation=u'utf8_bin', length=80), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Routine_name', mysql.CHAR(charset=u'utf8', length=64), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Routine_type', mysql.ENUM(u'FUNCTION', u'PROCEDURE', collation=u'utf8_bin'), nullable=False),
    sa.Column('Grantor', mysql.CHAR(collation=u'utf8_bin', length=141), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Proc_priv', mysql.SET(charset=u'utf8', length=13), server_default=sa.text(u"''"), nullable=False),
    sa.Column('Timestamp', mysql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('Host', 'Db', 'User', 'Routine_name', 'Routine_type'),
    mysql_collate=u'utf8_bin',
    mysql_comment=u'Procedure privileges',
    mysql_default_charset=u'utf8',
    mysql_engine=u'MyISAM'
    )
    op.drop_table('post')
    op.drop_table('blog')
    op.drop_table('category')
    op.drop_table('author')
    # ### end Alembic commands ###
