# This is a list of command-line arguments passed to a Python script when it is executed
import sys
print(sys.argv)

#sys.exit(Python exists and terminating the program. Its is commonly used this script program completed successfully or failed)
sys.exit("Goodbye!")

# sys.path
#(In this key useful for the search path and you can modify sys.path to add custom directories)
sys.path.append('/path/to/my/module')

# sys.version and sys.version_info
#(sys.version string containing of the version  and sys.version_info tuple gives details version info)
#(these attributes useful checking the python programmatically)
import sys
print(sys.version)  # Full version as a string
print(sys.version_info)  # Version info as a tuple

#sys.platform
#(this return the name of the platform such as,linux and macos)
import sys
print(sys.platform)

#sys.modules
#(this is useful for the show the all imported modules and loaded modules and useful for the debugging)
print(sys.modules)

# sys.getsizeof()
#it's return the size of an object in bytes
import sys
my_list = [1, 2, 3]
print(sys.getsizeof(my_list))

#sys.setrecursionlimit()
#increase recursion depth limit and when working with recursion algorithm
import sys
sys.setrecursionlimit(2000)  # Increase recursion depth limit






