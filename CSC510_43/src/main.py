import sys



the = {}   


class Main:
    """
    'the' - this configuration object is a dictionary which has some preset values 
    that could be used anywhere in the project use `from main import the` to import `the` object
    """
    the['eg'] = 'nothing'
    the['dump'] = False
    the['csvFilePath'] = '../data/data1.csv'
    the['nums'] = 512
    the['seed'] = 10019
    the['seperator'] = ','

    
    def mainFunction(argv):  
        """This function accepts the following cli arguments:
            -e      --eg            startup example                         
            -d      --dump          on test fail, exit with startdump       
            -f      --file          file with csv data                     
            -h      --help          show help                               
            -n      --nums          number of nums to keep                  
            -s      --seed          random number seed                      
            -S      --seperator     field seperator                         
        """
        opts = sys.argv
        for i, opt in enumerate(opts):
            if opt in ("-h", "--help"):
                print(
                    '''
                    =======================================

                    OPTIONS:
                    -e      --eg            startup example                         = nothing
                    -d      --dump          on test fail, exit with startdump       = false
                    -f      --file          file with csv data                      = data/data1.csv
                    -h      --help          show help                               = false
                    -n      --nums          number of nums to keep                  = 512
                    -s      --seed          random number seed                      = 10019
                    -S      --seperator     field seperator                         = ,]]

                    =======================================
                    '''
                )
                sys.exit()
            elif opt in ("-e", "--eg"):
                the['eg'] = opts[i+1]
            elif opt in ("-d", "--dump"):
                the['dump'] = True
            elif opt in ("-f", "--file"):
                the['csvFilePath'] = opts[i+1]
            elif opt in ("-n", "--nums"):
                the['nums'] = opts[i+1]
            elif opt in ("-s", "--seed"):
                the['seed'] = opts[i+1]
            elif opt in ("-S", "--seperator"):
                the['seperator'] = opts[i+1]


if __name__ == "__main__":
    Main.mainFunction(sys.argv[1:])
