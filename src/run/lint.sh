# Define the path to the modules directory
MODULES_DIR="../modules"

# Check if the modules directory exists
if [ ! -d "$MODULES_DIR" ]; then
  echo "The modules directory does not exist."
  exit 1
fi

# Iterate through all modules in the modules directory
for module in "$MODULES_DIR"/*; do
  # Check if the module is a directory
  if [ -d "$module" ]; then
    echo "-----------------------------------------"
    echo "Analyzing module $(basename "$module") :"
    echo "Mypy Analysis :"
    mypy "$module"
    echo "Pylint Analysis :"
    pylint "$module"
    echo "Analyze finish for $(basename "$module") :"
  fi
done

read -p "Press 'Enter' to quit"