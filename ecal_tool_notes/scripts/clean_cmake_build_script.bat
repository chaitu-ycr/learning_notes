set file_dir=%CD%
cd ..
set root_dir=%CD%
set build_dir=%root_dir%\build

if exist %build_dir% (
    rmdir /s /q %build_dir%
)
mkdir %build_dir%
cd %build_dir%

cmake .. -A x64
cmake --build . --parallel

cd %file_dir%
