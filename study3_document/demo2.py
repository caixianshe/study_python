# 文件的写入
# 特点一：在写入的模式下 如果文件不存在 那么系统会帮助我们进行创建文件
# 特点二：在写入的模式下 如果文件存在 那么写入前 会把里面的内容全部清空

# write是把内容写入到缓冲区

# 而close关闭 或者是 flush刷新 执行之后才是把缓冲区的内容 写入硬盘中 避免频繁的操作硬盘 降低效率 攒一堆 然后写入 加快效率

# 特点一demo：
# t = open("F:\workspace\python-study\study1.txt", "w", encoding="utf-8")
# t.write("你好啊，这是写入操作")
# t.flush()
# # close中内嵌了flush
# t.close()

# 特点二demo：
# t = open("F:\workspace\python-study\study1.txt", "w", encoding="utf-8")
# t.write("这是在文件存在的情况下进行写入")
# t.flush()
# t.close()

# 文件的追加
# 和前面的文件写入基本上一致 只不过是把w 改成a
t = open("F:\workspace\python-study/bill.txt", "a", encoding="utf-8")
t.write("。这是我追加的内容")
# t.flush()
t.close()
