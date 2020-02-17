
#continue:退出当前这一次循环
#在 continue 之前一定要修改计数器
i = 1

while i <= 5:
    if i == 3:
        print('吃到了虫子')
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
else:
    print('有的苹果里面是有虫子的')