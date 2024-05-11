// Runtime: 45ms, Beats 66.91% of users with c++
// Memory: 37.08MB, Beats 14.46% of users with c++


class ParkingSystem {
public:
    int big;
    int medium;
    int small;
    ParkingSystem(int big, int medium, int small) {
        this->big = big;
        this->medium = medium;
        this->small = small;
    }
    
    bool addCar(int carType) {
        if(carType == 1) {
            if(this->big) {
                this->big--;
                return true;
            }
            return false;
        }
        else if(carType == 2) {
            if(this->medium) {
                this->medium--;
                return true;
            }
            return false;
        }
        else {
            if(this->small) {
                this->small--;
                return true;
            }
            return false;
        }
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */