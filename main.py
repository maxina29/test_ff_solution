import json

class Entity:
  def __init__(self,name):
    self.name=name
  def __str__(self):
    return 'Сущность: ' + self.name


class Employee:
  def __init__(self,name,organization):
    self.name=name
    self.organization=organization
  def __str__(self):
    return f'{self.name} работает в {self.organization}'


if __name__ == '__main__':
    cat = Entity('Сугроб')
    print(cat)

    employee = Employee('Петя', 'Foxford')
    print(employee)

    json.dump([cat,employee],open('data.json','w'),default=vars)
