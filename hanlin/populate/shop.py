from populate import base
from shop.models import Branch, Plant


branches = ['景天', '龍舌蘭', '組盆']
plants = ['t001.jpg', 't002.jpg', 'shoppingcar.jpg']


def populate():
    print('Populating Branch and Plant ... ', end='')
    Branch.objects.all().delete()
    Plant.objects.all().delete()
    j=1
    for i in range(3):
        branchitem = Branch()
        branchitem.branchName = branches[i]
        branchitem.url = plants[i]
        branchitem.save()
        for plant in plants:
            plt = Plant()
            plt.branch=branchitem
            plt.plantName='t'+str(j)
            plt.code='plt'+str(j)
            plt.price=10
            plt.inventory=10
            plt.url=plant
            plt.save()
            j+=1
            
    print('done')


if __name__ == '__main__':
    populate()