class PIDController:
    def __init__(self, target_pos):
        self.target_pos = target_pos
        self.Kp = 0.0
        self.Ki = 0.0
        self.Kd = 0.0
        self.bias = 0.0
        self.previous_position = 0.0
        return

    def reset(self):
        return

#TODO: Complete your PID control within this function. At the moment, it holds
#      only the bias. Your final solution must use the error between the 
#      target_pos and the ball position, plus the PID gains. You cannot
#      use the bias in your final answer. 
    def get_fan_rpm(self, vertical_ball_position):
        error = (self.target_pos - vertical_ball_position)
        previous_error = (self.target_pos - self.previous_position)
        proportional = (self.Kp * error)
        integral = (self.Ki) * (error - previous_error)
        derivative = self.Kd * (vertical_ball_position - self.previous_position)
        output = proportional + integral + derivative
        self.previous_position = vertical_ball_position
        return output
