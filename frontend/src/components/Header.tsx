import "./index.css";
import axios from "axios";
import React from "react";
import { Button, Input, TextField } from "@mui/material";
import { Context } from "./SearchEngine";

function Header() {
  const [img, setImg] = React.useState(null);
  const [metaSearch, setMetaSearch] = React.useState("");
  const [imgToUpload, setImgToUpload] = React.useState(null);
  const { setImages } = React.useContext(Context);

  const handleSubmit = React.useCallback(async () => {
    const formData = new FormData();
    if (!img && !metaSearch) return;

    // formData.append("image", img);

    const payload: any = {};

    const res = await axios.post(
      "https://d32bdp38hd.execute-api.eu-central-1.amazonaws.com/images",
      img
    );

    if (res.data.url) payload.url = res.data.url;
    if (metaSearch) payload.metadata = metaSearch;

    const res2 = await axios.post("http://23.88.117.114/api/images/search", {
      payload,
    });

    setImages(res2.data);
  }, [img]);

  const handleUpload = React.useCallback(async () => {
    const formData = new FormData();
    if (!imgToUpload) return;
    formData.append("image", imgToUpload);

    const res = await axios.post(
      "https://d32bdp38hd.execute-api.eu-central-1.amazonaws.com/images",
      imgToUpload
    );

    const res3 = await axios.post("http://23.88.117.114/api/images", {
      url: res.data.url,
    });

    // const res2 = await axios.post("http://23.88.117.114/api/images/search", {
    //   url: res.data.url,
    // });

    alert("Added successful");
  }, [imgToUpload]);

  return (
    <div className="header-wrapper">
      <div className="wrap-wrap">
        <div className="wrap-wrap-2">
          <Input
            hidden
            type="file"
            // @ts-ignore
            onChange={(e) => setImg(e.target.files[0])}
          />

          <Button
            onClick={handleSubmit}
            variant="contained"
            className="upload-btn"
          >
            Search
          </Button>
        </div>

        <TextField
          style={{ marginTop: "20px" }}
          size="small"
          variant="outlined"
          label="Metedata search"
          onChange={(e) => setMetaSearch(e.target.value)}
        />
      </div>
      <div
        style={{
          marginLeft: "100px",
          marginRight: "100px",
          borderLeft: "3px solid #581845",
        }}
      />
      <Input
        hidden
        type="file"
        // @ts-ignore
        onChange={(e) => setImgToUpload(e.target.files[0])}
      />

      <Button onClick={handleUpload} variant="contained" className="upload-btn">
        Upload
      </Button>
    </div>
  );
}

export default Header;
