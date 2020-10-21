# 实验室的图片上传展示项目
第一个 Django 项目，学长和同学给了个前端模板和 Django 项目的模板然后边学边改。

# 安装

0. 需要先安装 anacnoda 。
1. 按照个人的习惯将项目导入 pycharm 中。
2. environment.yml 是该项目导出的 conda 环境。所以在 pycharm 中的命令行运行


```python
conda env create -f environment.yml
```

等待时间应该比较长，毕竟要下载相关的第三方包，耐心等待即可。

以下 3 和 4 是关于后台用哪个数据库的，选一个安装即可。

3. sqlite3：
  
   + 将 settings.py 中 Databases 段的 sqlite3 打开并且注释掉 mysql。
   + 并且 `__init__.py` 中不需要任何代码。
    
4. mysql8.0: 
  
   + 请先安装 mysql8.0。
   + 然后将 settings.py 中 `Databases` 字段的 mysql 的打开并且注释掉 sqlite3。
   + 在 mysql8.0 中先创建好你的数据库。然后将 `Databases` 字段中的 `PASSWORD` 和 `NAME` 更改为 mysql 的密码和数据库名。
   + 并且请打开 `__init__.py` 中的注释

# 运行

0. 如果是 mysql8.0：请确保 mysql8.0 服务启动并已创建了该数据库。
1. 导入的环境名为：myDjangoEnv，所以进入到环境中:

```python
activate  myDjangoEnv 

```

2. 在数据库中创建表:

    sqlite3 请使用:
    
    ```python
    python manage.py migrate
    ```
    mysql8.0 请使用:
    
    ```python
    python manage.py migrate --database=mysqlDB
    ```


3. 启动服务:
```python
python manage.py runserver
```

4. 浏览器 `127.0.0.1:8000` 访问

# 相关文章：

[第一次Django实战](https://mikasalee.github.io/2020/10/07/FirstDjangoDemo/)

# 日志：
2020-10-14：第一阶段任务完成：图片上传功能基本实现，接下来等待前端的同学把前端写完之后再次修改 view 层和 model层。
