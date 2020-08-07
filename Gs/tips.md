1. 清空控制台

   ```python
   oldstdout = sys.stdout
   ...
   sys.stdout = oldstdout
   os.system('cls')
   ```

   

2. 检测`ESCape`键

   ```python
   import msvcrt
   while True:
       ch = msvcrt.getch()  # esc -> b'\x1b' 
       if ch[0] == 27:  # esc[0] -> 27
           break
   ```

   esc[0]=27

   enter[0]=13

   space[0]=32

   w[0]=119

   s[0]=115

   a[0]=97

   d[0]=100

3. 查询特殊字符

   `Win10`运行，输入`charmap`

4. 字体颜色

   ```python
   print('\033[1;31;0m%s\033[0m' % str)
   ```

   其中`31`控制颜色

   ```
   31: 红色
   32：绿色
   33：褐色
   34：青色
   35：洋红
   36：翠绿
   37：灰色
   38：白色
   ```

   