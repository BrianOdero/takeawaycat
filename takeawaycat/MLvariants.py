import enum

class TypeExpr(enum.Enum):# class is an enum that represents the two possible kinds of type expressions: type variables and arrow types. 
  TYPE_VAR = 0
  ARROW = 1

class TypeVar:#Expresses the variable type expression
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

class ArrowType:#Expresses the arrowtype type expression
  def __init__(self, domain, codomain):
    self.domain = domain
    self.codomain = codomain

  def __str__(self):
    return f"{self.domain} -> {self.codomain}"

class MLTypeExpr:#MLTypeExpr and MLType classes represent ML type expressions, which are type expressions that may contain type variables. 
  def __init__(self, type_expr):
    self.type_expr = type_expr

  def __str__(self):
    return str(self.type_expr)

class MLType:
  def __init__(self, type_expr):
    self.type_expr = type_expr

  def __str__(self):
    return str(self.type_expr)

def createNewTypeVar():
  type_var_counter = 0
  while True:
    type_var_name = f"t{type_var_counter}"
    if type_var_name not in used_type_vars:
      used_type_vars.add(type_var_name)
      return TypeVar(type_var_name)
    type_var_counter += 1

used_type_vars = set()

#implementing no C
def __str__(self):
    if isinstance(self.type_expr, TypeVar):
        return self.type_expr.name
    elif isinstance(self.type_expr, ArrowType):
        return f"({self.type_expr.domain} -> {self.type_expr.codomain})"
    else:
        raise ValueError(f"Invalid type expression: {self.type_expr}")

type_expr1 = createNewTypeVar()
type_expr2 = createNewTypeVar()
type_expr3 = createNewTypeVar()

arrow_type = ArrowType(type_expr1, type_expr2)
arrow_type2 = ArrowType(arrow_type, type_expr3)

ml_type_expr = MLTypeExpr(arrow_type2)
ml_type = MLType(ml_type_expr)




print(ml_type)
