from django.shortcuts import render

# Create your views here.
def register(request):
  return render(request,'users/register.html')

def register_handle(request):
  username=request.POST.get('user_name')
  password=request.POST.get('pwd')
  email=request.POST.get('emali')

  if not all([username,password,email]):
    return render(request,'users/register.html',{'errmsg':'参数不能为空!'})


  if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
    return render(request,'users/register.html',{'errmsg':'邮箱不合法!'})

  try:
    Passport.objects.add_one_passport(username=username.password=password,email=email)
  except:
    return render(request,'users/register.html',{'errmsg':'用户名已存在！'})

  return redirect(reverse('user:register'))
