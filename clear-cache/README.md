# clear-cache
# 每6小时清理Linux相关缓存（0:00,6:00,12:00,18:00）
## 请在root用户下运行以下命令

### 下载clear-cache.sh脚本,保存在当前路径下

``` bash
curl -o clear-cache.sh -L https://raw.githubusercontent.com/Ccapton/myshell/master/clear-cache/clear-cache.sh && chmod +x clear-cache.sh 
```

### 执行clear-cache.sh脚本
``` bash
./clear-cache.sh
```

### 查看clear-cache进程
``` bash
ps aux|grep clear-cache
```