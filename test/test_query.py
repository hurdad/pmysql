import shutil
import os
import pytest
import subprocess


def test_select_column_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_column.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_all_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_all.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_distinct_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_distinct.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_alpha_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_alpha.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_num_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_num.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_and_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_and.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_or_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_or.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_or_and_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_or_and.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_orderby_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_orderby.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_orderby_desc_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_orderby_desc.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_orderby_multi_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_orderby_multi.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_insert_into_sql():
	proc = subprocess.Popen(['../pmysql', 'query/insert_into.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_update_set_where_sql():
	proc = subprocess.Popen(['../pmysql', 'query/update_set_where.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_delete_from_sql():
	proc = subprocess.Popen(['../pmysql', 'query/delete_from.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_like_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_like.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_in_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_in.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_where_between_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_where_between.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_column_alias_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_column_alias.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_table_alias_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_table_alias.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_join_inner_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_join_inner.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_join_left_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_join_left.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_join_right_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_join_right.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_join_full_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_join_full.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_union_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_union.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_db_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_db.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_table_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_table.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_table_not_null_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_table_not_null.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_table_unique_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_table_unique.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_table_primary_key_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_table_primary_key.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_table_foreign_key_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_table_foreign_key.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_index_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_index.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_index_list_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_index_list.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_drop_table_sql():
	proc = subprocess.Popen(['../pmysql', 'query/drop_table.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_drop_database_sql():
	proc = subprocess.Popen(['../pmysql', 'query/drop_database.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_truncate_table_sql():
	proc = subprocess.Popen(['../pmysql', 'query/truncate_table.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_alter_column_sql():
	proc = subprocess.Popen(['../pmysql', 'query/alter_column.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_alter_drop_column_sql():
	proc = subprocess.Popen(['../pmysql', 'query/alter_drop_column.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_create_table_auto_increment_sql():
	proc = subprocess.Popen(['../pmysql', 'query/create_table_auto_increment.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_avg_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_avg.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_count_column_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_count_column.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_count_all_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_count_all.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_sum_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_sum.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_join_group_by_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_join_group_by.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		

def test_select_join_group_by_multi_sql():
	proc = subprocess.Popen(['../pmysql', 'query/select_join_group_by_multi.sql'], stdout=subprocess.PIPE)
	tmp = proc.stdout.read()
	if tmp.find('SQL parse worked') == -1:
		print tmp
		raise Exception('SQL parse failed')
		
