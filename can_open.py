import canopen
import time


class CANOPEN():
    def __init__(self, port='can1', node_id=10, speed0=0):
        network = canopen.Network()
        network.connect(bustype='socketcan', channel=port)
        self.node = network.add_node(node_id, 'JD2xxx_v1.0.eds')
        

    def get_data_raw(self, ):
        x = self.node.sdo[0x3403].raw * accel_resolution
        y = self.node.sdo[0x3404].raw * accel_resolution
        z = self.node.sdo[0x3405].raw * accel_resolution
        return x,y,z

    def get_prop_accel_vector(self):
        x = self.node.sdo[0x3403].raw * accel_resolution
        y = self.node.sdo[0x3404].raw * accel_resolution
        z = self.node.sdo[0x3405].raw * accel_resolution

        f  = np.array([x,y,z]).T
        return f

    def get_gyro(self):
        x = self.node.sdo[0x3400].raw * gyro_resolution 
        y = self.node.sdo[0x3401].raw * gyro_resolution 
        z = self.node.sdo[0x3402].raw * gyro_resolution 
        return x,y,z

    def get_slopes(self):
        x = self.node.sdo[0x6010].raw * self.slope_resolution
        y = self.node.sdo[0x6020].raw * self.slope_resolution
        return x,y

    def get_rot_grav(self):
        ''' Rotated gravity '''
        thetax_deg, thetay_deg = self.get_slopes()
        thetax = thetay_deg*np.pi/180
        Rx = np.array([[1, 0, 0],
                    [0, np.cos(thetax), -np.sin(thetax)],
                    [0, np.sin(thetax), np.cos(thetax)]])

        thetay = -thetax_deg*np.pi/180
        Ry = np.array([[np.cos(thetay), 0, np.sin(thetay)],
                    [0, 1, 0],
                    [-np.sin(thetay), 0, np.cos(thetay)]])

        g_rotated = Ry@Rx@g_vector
        return g_rotated

    def get_accel(self):
        ''' Retorna el modulo de la aceleracion respecto al eje fijo, descontando el efecto de la gravedad
        en la aceleracion propia (proper acceleration)'''
        f = self.get_prop_accel_vector()
        g = self.get_rot_grav()
        r = f + g
        #r_norm = np.linalg.norm(r)
        return r

    def get_speed_stimation(self, iterations=4):
        start = time.time()
        accel_cumulative = 0
        for i in range(1,iterations+1):
            accel_raw = self.get_accel()
            accel_cumulative += accel_raw

        accel = accel_cumulative/iterations  
        accel = np.round(accel,1)    

        end = time.time()

        delta = end-start
        self.speed += accel*delta

        self.speed_norm = np.linalg.norm(self.speed[0:1])

        return self.speed_norm




