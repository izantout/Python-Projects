# COPY-PASTE YOUR Matrix AND Vec CLASSES TO THIS CELL. 
import math
class Vec:
    def __init__(self, contents = []):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
        return
    
    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        f = 0
        for i in self.elements:
            f += i**2 
        return math.sqrt(f)
       
        
    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("ERROR: Cannot add vectors of different lengths")
        f = []
        for x,y in zip(self.elements, other.elements):
            f.append(x + y)
        return Vec(f)
        
    
    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        
        if len(self.elements) != len(other.elements):
            raise ValueError("Cannot subtract vectors of different lengths")
        f = []
        for x,y in zip(self.elements, other.elements):
            f.append(x - y)
        return Vec(f)
        

    
    
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            #FIXME: IMPLEMENT
            if len(self.elements) != len(other.elements):
                raise ValueError("Cannot multiply vectors of different lengths")
            f = 0
            for i in range(len(self.elements)):
                f += self.elements[i] * other.elements[i]
            return f

        
        

        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            #FIXME: IMPLEMENT
            f = []
            for x in self.elements:
                f.append(x * other)
            return Vec(f)
            
    
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        if type(other) == float or type(other) == int: 
            f = []
            for x in self.elements:
                f.append(x * other)
            return Vec(f)
    

    
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation

class Matrix:
    
    def __init__(self, final = []): 
        self.rows = final
        self.cols = []
        for i in range(len(self.rows)):
            self.cols.append(self.rows[i][0])
    
    def __add__(self, other):
        if len(other.rows) == len(self.rows) and len(other.rows[0]) == len(self.rows[0]):
            nMatrix = []
            for i in range(len(self.rows)):
                nRow = []
                for j in range(len(self.rows[i])):
                    nRow.append(self.rows[i][j] + other.rows[i][j])
                nMatrix.append(nRow)
            return Matrix(nMatrix)
        else:
            raise ValueError("ERROR: Cannot add matrices of different dimensions.")
    
    def __sub__(self, other):
        if len(other.rows) == len(self.rows) and len(other.rows[0]) == len(self.rows[0]):
            nMatrix = []
            for i in range(len(self.rows)):
                nRow = []
                for j in range(len(self.rows[i])):
                    nRow.append(self.rows[i][j] - other.rows[i][j])
                nMatrix.append(nRow)
            return Matrix(nMatrix)
        else:
            raise ValueError("ERROR: Cannot add matrices of different dimensions.")
    
    def __mul__(self, other):  
        if type(other) == float or type(other) == int:
            nMatrix = []
            for i in range(len(self.rows)):
                nRow = []
                for j in range(len(self.rows[i])):
                    nRow.append(self.rows[i][j] * other)
                nMatrix.append(nRow)
            return Matrix(nMatrix)
        elif type(other) == Matrix:
                nMatrix = []
                if len(self.rows[0]) == len(other.rows):
                    for i in range(len(self.rows)):
                        nRow = []
                        for j in range(len(other.rows[0])):
                            nRow.append(0)
                            for k in range(len(self.rows[i])):
                                nRow[j] += self.rows[i][k] * other.rows[k][j]
                        nMatrix.append(nRow)
                    return Matrix(nMatrix)
                else:
                    raise ValueError("ERROR: Cannot multiply matrices of different dimensions.")
        elif type(other) == Vec:
            nMatrix = []
            for i in range(len(self.rows)):
                sum = 0
                for j in range(len(self.rows[0])):
                    sum += self.rows[i][j] * other.elements[j]
                nMatrix.append(sum)
            return Vec(nMatrix)
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other):  
        if type(other) == float  or type(other) == int:
                nMatrix = []
                for i in range(len(self.rows)):
                    nRow = []
                    for j in range(len(self.rows[i])):
                        nRow.append(self.rows[i][j] * other)
                    nMatrix.append(nRow)
                return Matrix(nMatrix)
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __str__(self):
       
        string = ""
        for i in range(len(self.rows)):
            string += "["
            for j in range(len(self.rows[i])):
                string += str(self.rows[i][j]) + ", "
            string = string[:-2] + "]\n"
        
        return string
            
        
    def __eq__(self, other):
        this_rows = self.row_space()
        other_rows = other.row_space()
        this_cols = self.col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols

    def __req__(self, other):
        this_rows = self.row_space()
        other_rows = other.row_space()
        this_cols = self.col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols

    def set_col(self,j,u):
        if len(u) != len(self.rows):
            raise ValueError("Incompatible column length.")
        for i in range(len(self.rows)):
            self.rows[i][j-1] = u[i]
    
    def set_row(self,i,v):
        if len(v) != len(self.rows[0]):
            raise ValueError("Incompatible row length.")
        self.rows[i-1] = v
    
    def set_entry(self,i,j,x):
        self.rows[i-1][j-1] = x

    def get_col(self,j):
        return list([self.rows[i][j-1] for i in range(len(self.rows))])

    def get_row(self,i):
        return list([self.rows[i-1][j] for j in range(len(self.rows[0]))])

    def get_entry(self,i,j):
        return self.rows[i-1][j-1]
    
    def col_space(self):
        col_space = [0]*len(self.rows[0])
        for i in range(len(self.rows[0])):
            col_space[i] = (self.get_col(i+1))
        return col_space
    
    def row_space(self):
        row_space = []
        for i in range(len(self.rows)):
            row_space.append((self.get_row(i+1)))
        return row_space
    
    def get_diag(self,k):
        diag = []
        if k == 0:
            for i in range(len(self.rows)):
                diag.append(self.rows[i][i])
            return diag
        elif k > 0:
            for i in range(len(self.rows) - k):
                diag.append(self.rows[i][i+k])
            return diag
        else:
            for i in range(len(self.rows) +k):
                diag.append(self.rows[i-k][i])
            return diag
