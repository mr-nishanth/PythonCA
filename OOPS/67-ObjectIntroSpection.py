class Employee:
    def __init__(self,fname,lname):
        self.firstname = fname
        
        self.lastname =lname
        #self.email = f"{fname}.{lname}@gmail.com" # ==> 1
    @property # 2
    def email(self):
        if self.firstname == None or self.lastname == None:  # ==> 5
            return "Email is not set"
        return f"{self.firstname}{self.lastname}@gmail.com"
    @email.setter
    def email(self, string):
        names = string.split("@")[0]  # [csk.007,gmail.com]
        # names=names[0] or string.split("@")[0] both are same
        self.firstname=names.split(".")[0]  # [csk,007]
        self.lastname = names.split(".")[1]
    @email.deleter # 4
    def email(self):
        self.firstname = None
        self.lastname =None

    def explain(self):
        return f"This Employee name is {self.firstname} {self.lastname}"
    def __str__(self):
        return "I am String"

Nisha=Employee("Black","Pearl")
print(Nisha.email)
print(type(Nisha))
print(id(Nisha))
print(dir(Nisha))

import inspect

#print(inspect.getmembers(Nisha))
print(dir(inspect))
# 'abc', 'ast', 'attrgetter', 'builtins', 'classify_class_attrs', 'cleandoc', 'collections', 'currentframe', 'dis', 'enum', 'findsource', 'formatannotation', 'formatannotationrelativeto', 'formatargspec', 'formatargvalues', 'functools', 'getabsfile', 'getargs', 'getargspec', 'getargvalues', 'getattr_static', 'getblock', 'getcallargs', 'getclasstree', 'getclosurevars', 'getcomments', 'getcoroutinelocals', 'getcoroutinestate', 'getdoc', 'getfile', 'getframeinfo', 'getfullargspec', 'getgeneratorlocals', 'getgeneratorstate', 'getinnerframes', 'getlineno', 'getmembers', 'getmodule', 'getmodulename', 'getmro', 'getouterframes', 'getsource', 'getsourcefile', 'getsourcelines', 'importlib', 'indentsize', 'isabstract', 'isasyncgen', 'isasyncgenfunction', 'isawaitable', 'isbuiltin', 'isclass', 'iscode', 'iscoroutine', 'iscoroutinefunction', 'isdatadescriptor', 'isframe', 'isfunction', 'isgenerator', 'isgeneratorfunction', 'isgetsetdescriptor', 'ismemberdescriptor', 'ismethod', 'ismethoddescriptor', 'ismodule', 'isroutine', 'istraceback', 'itertools', 'k', 'linecache', 'mod_dict', 'modulesbyfile', 'namedtuple', 'os', 're', 'signature', 'stack', 'sys', 'token', 'tokenize', 'trace', 'types', 'unwrap', 'v', 'walktree', 'warnings'