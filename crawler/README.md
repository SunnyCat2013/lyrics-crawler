想要使用这个东西
1. 安装 postgres
2. 修改 `./db_operations.py` 里面的 `database`, `user`, `password`
3. 在本地手动创建 database 'lyrics' 和 table 'songs'


# 导出到 csv
sudo -u postgres psql
\c lyrics
copy (select * from songs) to '/path/to/export' with csv delimiter ',';
# 参考
命令
http://www.cnblogs.com/z-sm/archive/2016/07/05/5644165.html
