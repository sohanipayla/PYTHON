n=int(input('enter number:'))
gusses=int(input('enter number of gusses:'))
gusses=n/2
for i in range(gusses):
    if gusses**2==n:
        break
    gusses=(gusses*n/gusses)/2
print(gusses)