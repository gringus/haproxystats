"""
haproxstats.metrics
~~~~~~~~~~~~~~~~~~

This module provides the field names contained in the HAProxy statistics.
"""
DAEMON_METRICS = [
    'CompressBpsIn',
    'CompressBpsOut',
    'CompressBpsRateLim',
    'ConnRate',
    'ConnRateLimit'
    'CumConns',
    'CumReq',
    'CumSslConns',
    'CurrConns',
    'CurrSslConns',
    'Hard_maxcon',
    'MaxConnRate',
    'MaxSessRate',
    'MaxSslConns',
    'MaxSslRate',
    'MaxZlibMemUsage',
    'Maxconn',
    'Maxpipes',
    'Maxsock',
    'Memmax_MB',
    'PipesFree',
    'PipesUsed',
    'Run_queue',
    'SessRate',
    'SessRateLimit',
    'SslBackendKeyRate',
    'SslBackendMaxKeyRate',
    'SslCacheLookups',
    'SslCacheMisses',
    'SslFrontendKeyRate',
    'SslFrontendMaxKeyRate',
    'SslFrontendSessionReuse_pct',
    'SslRate',
    'SslRateLimit',
    'Tasks',
    'Ulimit-n',
    'Uptime_sec',
    'ZlibMemUsage',
]

DAEMON_AVG_METRICS = [
    'Idle_pct',
]
AVG_METRICS = [
    'act',
    'bck',
    'check_duration',
    'ctime',
    'downtime',
    'qlimit',
    'qtime',
    'rtime',
    'throttle',
    'ttime',
    'weight',
]
SERVER_METRICS = [
    'qcur',
    'qmax',
    'scur',
    'smax',
    'stot',
    'bin',
    'bout',
    'dresp',
    'econ',
    'eresp',
    'wretr',
    'wredis',
    'chkfail',
    'lbtot',
    'rate',
    'rate_max',
    'hrsp_1xx',
    'hrsp_2xx',
    'hrsp_3xx',
    'hrsp_4xx',
    'hrsp_5xx',
    'hrsp_other',
    'cli_abrt',
    'srv_abrt',
]
SERVER_AVG_METRICS = [
    'qtime',
    'rtime',
    'throttle',
    'ttime',
    'weight',
]
BACKEND_METRICS = [
    'act',
    'bck',
    'bin',
    'bout',
    'chkdown',
    'cli_abrt',
    'comp_byp',
    'comp_in',
    'comp_out',
    'comp_rsp',
    'downtime',
    'dreq',
    'dresp',
    'econ',
    'eresp',
    'hrsp_1xx',
    'hrsp_2xx',
    'hrsp_3xx',
    'hrsp_4xx',
    'hrsp_5xx',
    'hrsp_other',
    'lbtot',
    'qcur',
    'qmax',
    'rate',
    'rate_max',
    'scur',
    'slim',
    'smax',
    'srv_abrt',
    'stot',
    'wredis',
    'wretr',
]
BACKEND_AVG_METRICS = [
    'rtime',
    'ctime',
    'qtime',
    'ttime',
    'weight',
]
FRONTEND_METRICS = [
    'bin',
    'bout',
    'comp_byp',
    'comp_in',
    'comp_out',
    'comp_rsp',
    'dreq',
    'dresp',
    'ereq',
    'hrsp_1xx',
    'hrsp_2xx',
    'hrsp_3xx',
    'hrsp_4xx',
    'hrsp_5xx',
    'hrsp_other',
    'rate',
    'rate_lim',
    'rate_max',
    'req_rate',
    'req_rate_max',
    'req_tot',
    'scur',
    'slim',
    'smax',
    'stot',
]
