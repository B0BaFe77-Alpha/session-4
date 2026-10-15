class RobotBase:
    """blueprint for the base code fo rhe robot"""
    def __init__ (self, name, battery_level, is_moving, sensor_readings):
        """Initialize the varibles and make them read only
        Args:
            name: Name of the robot (str)
            battery_name: how much battery chargew the robot has (float must be >= 0)
            is_moivng: whether its moving or not (bool)
            sensor_readings: what the sensors are "seeing" (dict) 
        
        """
        self._name = name
        self._battery_level = battery_level

        self._is_moving = is_moving 
        self._sensor_readings = sensor_readings
        @property
        def name(self):
            """gets the name of the robot"""
            return self._name
        @property
        def battery_level(self):
                """gets the battery level of the robot"""
                return self._battery_level
        @property
        def is_moving(self):
                """gets whether or not the robot it moving"""
                
                    
                return self._is_moving 
        @property
        def sensor_readings(self):
                """gets what the robot sensers"""
                return self._sensor_readings

        
        @battery_level.setter
        def battery_level(self, charge):
            """Set new battery level as it depletes with validation.
                Args:
                    charge new battery level

                Raises:
                        ValueError is value negative
            """
            if charge < 0 :
                raise  ValueError("CANNOT HAVE NEGATIVE CHARGE")
            elif charge > 100:
                 raise ValueError("CANNOT HAVE CHARGE ABOVE 100")
            self._battery_level = charge



        @is_moving.setter
        def is_moving(self):
            """ checks to see if the robots movign and acts accordingly
            Args:
                is_moving to see if it is moving and which function too call
            Raises:
                no need for valueErrors at thsi point.
            """
            if self._is_moving == True:
                self.move_forward
            else:
                self.stop()


    def stop(self ):
                """a stopped stae for the robot to be in. makes _is_moving fasle 
            Args:
                NONE 
            Raises:
            also none 
    
                
                """
                self._is_moving = False 
                return self._is_moving
    
    def move_forward(self, speed: int):
          """ checks to see if the robot is moving forward 
          Args:
            speed: how quickly is moves forward ( authors note rather then make a negitive speed go backwords i woudl just make new function for that)
          Raises: 
            ValueError if value is negitive or 0.
          """    
          if  self._battery_level == 0:
                self.stop()
          elif speed <= 0:
            raise ValueError("speed cannot be 0 or lower")
          elif speed > self._battery_level:
               self._battery_level = 0
               self.stop()
          else:
                self._battery_level -= speed
                self._is_moving = True
                return speed 

    def get_sensor_reading(self, name):
          """ gets the name and adds  it to the dictionary and returns none if their isn't anything htere
          Args:
            name: the name to be added
            
          """
  
          if name in self._sensor_readings:
              return self._sensor_readings[name] 
          else:
            return None

    def set_sensor_reading(self, name, value):
        """ gets the data and sends it to the dictionary
        Args:
            name: the sensor reading to be added
        Raises:
            ValueError: if there is no data to add.

        """
        if name in self._sensor_readings:
            self._sensor_readings[name] = value
        else:
            raise ValueError("no value recorded")
    def report_status(self):
        """a status report on the robot
         
         Returns:
         status as a string with all the robots info (str)
        """
        return(f"name:{self._name} | "
               f"the sensor readings {self._sensor_readings} | "
                #  f" if its moving{self._is_moving} | "
                #     f" the battery level {self._battery_level} " 
                )    

    def __str__(self):
        """Return user-friendly string representation."""
        return (f"name{self._name}, "
                f" readings{self._sensor_readings}" 
                f" moving{self._is_moving} "
                f"  battery level {self._battery_level} " ) 

    def __repr__(self):
        """Return developer-friendly string representation."""
        return (f"robot_name='{self._name}', "
                f"readings='{self._sensor_readings}', "
                f"moving={self._is_moving}, "
                f"battery level={self._battery_level})")                
            
         
                    
        
          
    
           

          
          
          
          
          
