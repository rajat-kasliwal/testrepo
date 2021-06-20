import math

stan=[5,6,8,10,12,14,16,18,20,22,25,28,30,32,35,40,45,50,55,60,65,70,75,80,90,100,110,120,140,160,180,200]



def rod(roddia):
    
    for i in stan:
        if roddia>i:
            pass
        else:
            return i
            break


while True:  

	p=float(input('Enter axial load (in Newtons): ' ))

	fs=float(input('Enter factor of safety: '))

	ys=float(input('Enter Yield strength of material (in MPa): '))

	#DIMENSIONS
	ten=ys/fs
    
	com=ys/fs
    
	sher=ys/(2*fs)

	dia=rod((4*p/math.pi/ten)**0.5)

	endia=1.1*dia

	a=0.75*dia

	b=1.25*dia

	x= (2*p/math.pi/sher)**0.5

	y=(16*p/(math.pi*com)*(b/4+a/3))**(1/3)

	pindia= rod(max(x,y))

	d0=2*pindia

	d1= 1.5*pindia

	#CHECKING STRESSES

	# EYE

	eyeten= p/b/(d0-pindia)

	eyecomp= p/b/pindia

	eyesher= eyeten


	if ten>=eyeten:
    	print('Eye is safe in tension.')
	else:
    	print('eye fails in tension.')
    
	if com>=eyecomp:
    	print('Eye is safe in compression.')
	else:
    	print('eye fails in compression.')
        
	if sher>=eyesher:
    	print('Eye is safe in shear.')
	else:
    	print('eye fails in shear.')

    
	#FORK

	forten=p/((2*a)*(d0-pindia))

	forcom= p/(2*a*pindia)

	forsher= forten

	if ten>=forten:
    	print('Fork is safe in tension')
	else:
    	print('Fork fails in tension')
    

	if com>=forcom:
    	print('Fork is safe in compression')
	else:
    	print('Fork fails in compression')
    
    
	if sher>=forsher:
    	print('Fork is safe in shear')
	else:
    	print('Fork fails in shear')
    
    
	print('Dimensions of knuckle joint are: ')
	print('Rod diametre: %d' %dia)
	print('Enlarged diametre: %3.3f' %endia)
	print('Pin diametre: %3.3f' %pindia)
	print('a: %3.3f' %a)
	print('b: %3.3f' %b)

	repeat=input('another one? yes or no  ')
    
    if repeat.lower()=='yes':
        continue
    else:
        break