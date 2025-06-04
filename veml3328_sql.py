import datetime
from typing import Tuple

try:
    import smbus2
except ImportError:  # type: ignore
    smbus2 = None  # smbus2 is required for I2C access

try:
    import pyodbc
except ImportError:  # type: ignore
    pyodbc = None  # pyodbc is required for SQL Server access

I2C_BUS = 1
I2C_ADDRESS = 0x10  # Update with the correct VEML3328 I2C address

# Example register addresses for the RGB channels. These values may need to be
# adjusted according to the sensor's datasheet.
REG_RED = 0x08
REG_GREEN = 0x09
REG_BLUE = 0x0A


def read_rgb() -> Tuple[int, int, int]:
    """Read RGB values from the VEML3328 sensor."""
    if smbus2 is None:
        raise ImportError("smbus2 library is required to read from VEML3328")

    bus = smbus2.SMBus(I2C_BUS)
    red = bus.read_word_data(I2C_ADDRESS, REG_RED)
    green = bus.read_word_data(I2C_ADDRESS, REG_GREEN)
    blue = bus.read_word_data(I2C_ADDRESS, REG_BLUE)
    return red, green, blue


def save_to_sql_server(conn_str: str, rgb: Tuple[int, int, int]) -> None:
    """Save the RGB tuple to a SQL Server database."""
    if pyodbc is None:
        raise ImportError("pyodbc library is required to connect to SQL Server")

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(
        """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='VemlReadings' AND xtype='U')
        CREATE TABLE VemlReadings (
            id INT IDENTITY(1,1) PRIMARY KEY,
            timestamp DATETIME,
            red INT,
            green INT,
            blue INT
        )
        """
    )
    conn.commit()

    cursor.execute(
        "INSERT INTO VemlReadings (timestamp, red, green, blue) VALUES (?, ?, ?, ?)",
        datetime.datetime.now(), rgb[0], rgb[1], rgb[2]
    )
    conn.commit()
    conn.close()


def main() -> None:
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Sensors;"
        "UID=user;PWD=password"
    )

    rgb = read_rgb()
    save_to_sql_server(conn_str, rgb)
    print(f"Saved RGB values: {rgb}")


if __name__ == "__main__":
    main()
