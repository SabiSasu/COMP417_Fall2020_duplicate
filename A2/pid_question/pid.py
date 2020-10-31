import time
class PIDController:
    def __init__(self, target_pos):
        self.target_pos = target_pos
        self.Kp = 0.0
        self.Ki = 0.0
        self.Kd = 0.0
        self.bias = 0.0
        self.previous_error = 0.0
        self.previous_integral = 0.0
        self.current_time = time.time()
        self.last_time = self.current_time
        return

    def reset(self):
        return

#TODO: Complete your PID control within this function. At the moment, it holds
#      only the bias. Your final solution must use the error between the 
#      target_pos and the ball position, plus the PID gains. You cannot
#      use the bias in your final answer. 
    def get_fan_rpm(self, vertical_ball_position):
        error = (self.target_pos - vertical_ball_position)
        proportional = (self.Kp * error)
        self.current_time = time.time()
        delta_time = self.current_time - self.last_time
        integral = (self.previous_integral + error * delta_time)
        derivative = (error - self.previous_error)/ delta_time
        output = proportional + (self.Ki * integral) + (self.Kd * derivative)
        self.previous_error = error
        self.previous_integral = integral
        self.last_time = self.current_time
        return output
