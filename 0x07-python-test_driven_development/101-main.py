#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

#print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
#print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

#print(lazy_matrix_mul("hola", [[1, 2], [3, 4]]))
#lazy_matrix_mul(1, [[1, 2], [3, 4]])
#lazy_matrix_mul([[1, 2], [3, 4]], 1)

#m_a = [[1, 2], [3, 4]]
#m_b = [[1, 2], [3, 4]]
#lazy_matrix_mul(m_a + [1], m_b)


#m_a = [[1, 2], [3, 4]]
#m_b = [[3, 4]]
#lazy_matrix_mul(m_a, m_b)


#m_a = [["paula", 2], [3, 4]]
#m_b = [[1, 2], [3, 4]]
#lazy_matrix_mul(m_a, m_b)

#m_a = [[1, 2], [3]]
#m_b = [[1, 2], [3, 4]]
#lazy_matrix_mul(m_a, m_b)

#m_a = []
#m_b = [[1,2,3], [4, 5, 6]]
#lazy_matrix_mul(m_a, m_b)

#m_b = []
#m_a = [[1,2,3], [4, 5, 6]]
#lazy_matrix_mul(m_a, m_b)


m_a = [[]]
m_b = [[1,2,3], [4, 5, 6]]
lazy_matrix_mul(m_a, m_b)







