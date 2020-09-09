
sample_time = 0.01
time_end = 20
model = Bicycle()
solution_model = BicycleSolution()

# set delta directly
model.delta = np.arctan(2/10)
solution_model.delta = np.arctan(2/10)

t_data = np.arange(0,time_end,sample_time)
x_data = np.zeros_like(t_data)
y_data = np.zeros_like(t_data)
x_solution = np.zeros_like(t_data)
y_solution = np.zeros_like(t_data)

for i in range(t_data.shape[0]):
    x_data[i] = model.xc
    y_data[i] = model.yc
    model.step(np.pi, 0)
    
    x_solution[i] = solution_model.xc
    y_solution[i] = solution_model.yc
    solution_model.step(np.pi, 0)

#     print("model.xc = ",model.xc)
#     print("model.yc = ",model.yc)
#     print("model.theta = ",model.theta)
#     print("model.delta = ",model.delta)
#     print("model.beta = ",model.beta)
    
#     print("------------------------------------")
    
#     print("solution_model.xc = ",solution_model.xc)
#     print("solution_model.yc = ",solution_model.xc)
#     print("solution_model.theta = ",solution_model.theta)
#     print("solution_model.delta = ",solution_model.delta)
#     print("solution_model.beta = ",solution_model.beta)
    
#     print("---------------------------------------------")
    
    model.beta = 0
    solution_model.beta=0
    
plt.axis('equal')
plt.plot(x_data, y_data,label='Learner Model')
# plt.plot(x_solution, y_solution,label='Solution Model')
plt.legend()
plt.show()