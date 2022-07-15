def pathfinder(dir,file,path=""):
    for f in dir.keys():
        if f == file:
            path += '/' +  f
            return path
        else:
            if f[0] =='/':
                if path:
                    path += f
                else:
                    path = f
                #print(f,path)
                path = pathfinder(dir[f],file,path)
                if path != None:
                    return path
    return None

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

print(pathfinder(desktop, 'app_academy_logo.svg'))   
print(pathfinder(desktop, 'everlong.flac'))            
print(pathfinder(desktop, 'sequoia.jpeg')) # False