# Find a filename within a json directory structure. Here the base case is finding a single file. Then use recursion to check file within each directory.
def fileFinder(dir,file):
    if file in dir.keys():
        return True
    for f in dir.keys():
        if f[0]=='/':
            #print(f)
            if fileFinder(dir[f],file):
                return True
    return False

desktop = {
     '/images': {
         'app_academy_logo.svg': "",
         '/parks': {
             'yosemite.jpeg': "",
             'acadia.jpeg': "",
             'yellowstone.png': ""
         },
         '/pets': {
             'trixie_lou.jpeg': "",
             'rolo.jpeg': "",
             'opal.jpeg': "",
             'diana.jpeg': "",
         }
     },
     '/music': {
         'hey_programmers.mp3': "",
         '/genres': {
             '/rock': {
                 'everlong.flac': "",
                 'livin_on_a_prayer.mp3': ""
             },
             '/hip_hop': {
                 'express_yourself.wav': "",
                 'ny_state_of_mind.mp3': ""
             }
         }
     }
 }

print(fileFinder(desktop, 'app_academy_logo.svg'))   
print(fileFinder(desktop, 'everlong.flac'))            
print(fileFinder(desktop, 'sequoia.jpeg')) # False