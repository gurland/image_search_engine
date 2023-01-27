import axios from "axios";
import React from "react";
import Header from "./Header";
import Images from "./Images";
import Box from "@mui/material/Box";
import Tab from "@mui/material/Tab";
import TabContext from "@mui/lab/TabContext";
import TabList from "@mui/lab/TabList";
import TabPanel from "@mui/lab/TabPanel";
import "./index.css";
import ImageSearchPage from "./ImageSearchPage";
import UploadPage from "./UploadPage";
import MetadataPage from "./MetadataPage";
import ObjectDetection from "./ObjectDetection";

export const Context = React.createContext<any>(null);

function SearchEngine() {
  const [images, setImages] = React.useState([]);
  const [value, setValue] = React.useState("1");

  const handleChange = (event: React.SyntheticEvent, newValue: string) => {
    setValue(newValue);
  };

  const getImages = React.useCallback(async () => {}, []);

  React.useEffect(() => {
    getImages();
  }, []);

  return (
    <Context.Provider value={{ images, setImages }}>
      <TabContext value={value}>
        <Box
          style={{ marginTop: "30px" }}
          sx={{ borderBottom: 1, borderColor: "divider" }}
        >
          <TabList onChange={handleChange} aria-label="lab API tabs example">
            <Tab label="Images search" value="1" />
            <Tab label="Metadata search" value="2" />
            <Tab label="Object detection" value="3" />
            <Tab label="Upload image" value="4" />
          </TabList>
        </Box>
        <TabPanel value="1">
          <ImageSearchPage />
        </TabPanel>
        <TabPanel value="2">
          <MetadataPage />
        </TabPanel>
        <TabPanel value="3">
          <ObjectDetection />
        </TabPanel>
        <TabPanel value="4">
          <UploadPage />
        </TabPanel>
      </TabContext>
      {/* <div className="main-wrapper">
        <Header />
        <Images images={images} />
      </div> */}
    </Context.Provider>
  );
}

export default SearchEngine;
