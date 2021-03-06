#!/usr/bin/env python
#-*- coding:utf-8 -*-
urls = (
        '/(|login|index)/?',         'view.index.Login',      # 匹配：/,/index,/index/,/login,/login/,但是login函数要做冗余参数处理，还不知道为什么
        '/logout',                   'view.index.Logout',
        '/dashboard/?',              'view.adminCenter.Dashboard',  # /? 匹配最后面的斜杠，可有可无
        '/dashboard/IndexData',      'view.adminCenter.IndexData',  # 加载首页数据url
        '/project/?',                'view.project.Index',
        '/project/page',                'view.project.Index',
        '/project/add/?',            'view.project.Add',
        '/project/del/?',            'view.project.Del',
        '/project/config',           'view.project.Config',
        '/users/?',                  'view.users.Index',
        '/users/add/?',              'view.users.Add',
        '/users/del',                'view.users.Delete',
        '/users/enable',             'view.users.Enable',
        '/users/disable',            'view.users.Disable',
        '/users/edit',               'view.users.Edit',
        '/users/password',           'view.users.Password',
        #'^/users/([^/]+)$',         'view.users.%s',
        '/hosts/?',                  'view.hosts.Index',
        '/hosts/add/?',              'view.hosts.Add',
        '/hosts/edit',               'view.hosts.Edit',
        '/hosts/del',                'view.hosts.Del',
        #'/hosts/redis/?',           'view.redisAdmin.Index',
        #'/hosts/redis/add',         'view.redisAdmin.Add',
        #'/hosts/redis/edit',        'view.redisAdmin.Edit',
        #'/admin/redis',             'view.adminCenter.Redis',
        '/options',                  'view.options.Option',
        #'/admin/Delops',            'view.adminCenter.Delops',
        #'/admin/options/Delops',    'view.adminCenter.Delops',
        '/options/del',              'view.options.Del',
        '/options/page',             'view.options.Option',
        '/options/enable',           'view.options.Enable',
        '/options/disable',          'view.options.Disable',
        '/monitor/redis',            'view.monitor.M_Redis',
        '/monitor/mysql',            'view.monitor.M_MySQL',
        '/monitor/traffic',          'view.monitor.M_Traffic',
        '/salt/status',              'view.saltAdmin.Status',
        '/salt/minion_status',       'view.saltAdmin.Minion_status',
        '/salt/cmd',                 'view.saltAdmin.Cmd',
        #'/report',                  'view.report.Index',
        '/report/fault',             'view.report.Fault',
        '/report/add',               'view.report.Add',
        '/report/del',               'view.report.Del',
        #'/report/topo',             'view.report.Topo',
        '/report/releaselog',        'view.report.Releaselog',
        '/report/querysqllog',       'view.report.Querysqllog',
        '/db/sqltest',               'view.querydb.Sql_test',
        '/db/choose',                'view.querydb.Choose',
        '/db/sql_onput',             'view.querydb.Sql_onput',
        '/nginx/pool',               'view.pool.Pool',
        '/nginx/pool_node',          'view.pool.Pool_node',
        '/nginx/action',             'view.pool.Action',
        '/encryption',               'view.encryption.Index',
        '/test',                     'view.index.Test',
)
