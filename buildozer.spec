[app]

# (str) Title of your application
title = Darah Tinggi Simulator

# (str) Package name
package.name = darahtinggi

# (str) Package domain (needed for android packaging)
package.domain = org.emosi

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source directory
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Automatically accept Android SDK license agreement
android.accept_sdk_license = True

# (bool) Use --private data storage (True) or --public storage (False)
android.private_storage = True
