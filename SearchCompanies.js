import React from "react";
import companyData from "./company_info";
import CanvasJSReact from "./canvasjs/canvasjs.react";
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class SearchCompanies extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      inputValue: "",
      one: [],
      two: [],
      three: [],
      currentCompanyInfo: {},
      currentYear: "one",
      dataPointsOne: [],
      dataPointsTwo: [],
      dataPointsThree: [],
      allCompanies: []
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSumbit = this.handleSumbit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({ currentYear: event.target.value });
  }

  handleInputChange(event) {
    event.preventDefault();
    this.setState({ inputValue: event.target.value });
  }

  handleSumbit(event) {
    event.preventDefault();
    const body = { company: this.state.inputValue };
    fetch("/investment", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body)
    })
      .then(data => {
        if (data.status === 200) {
          return data.clone().json();
        } else {
          throw new Error("error cannot get data");
        }
      })
      .then(res => {
        if (res[0]["error"]) return;
        this.setState({ inputValue: "" });
        this.setState({ one: [] });
        this.setState({ two: [] });
        this.setState({ three: [] });
        this.setState({ dataPointsOne: [] });
        this.setState({ dataPointsTwo: [] });
        this.setState({ dataPointsThree: [] });
        this.setState({ one: res[1]["1Y"] });
        this.state.one.forEach((arr, index) => {
          this.setState(prevState => {
            let newState = [
              ...prevState.dataPointsOne,
              { x: index, y: arr["close"] }
            ];
            prevState.dataPointsOne = newState;
          });
        });

        this.setState({ two: res[1]["2Y"] });
        this.state.two.forEach((arr, index) => {
          this.setState(prevState => {
            let newState = [
              ...prevState.dataPointsTwo,
              { x: index, y: arr["close"] }
            ];
            prevState.dataPointsTwo = newState;
          });
        });
        this.setState({ three: res[1]["3Y"] });
        this.state.three.forEach((arr, index) => {
          this.setState(prevState => {
            let newState = [
              ...prevState.dataPointsThree,
              { x: index, y: arr["close"] }
            ];
            prevState.dataPointsThree = newState;
          });
        });
        this.setState({ currentCompanyInfo: res[0] });
      });
  }

  getDataPoints() {
    if (this.state.currentYear === "one") return this.state.dataPointsOne;
    if (this.state.currentYear === "two") return this.state.dataPointsTwo;
    if (this.state.currentYear === "three") return this.state.dataPointsThree;
  }

  generateGraph() {
    const options = {
      animationEnabled: true,
      exportEnabled: true,
      theme: "light2",
      title: {
        text: "Stock Price"
      },
      axisY: {
        title: "Closing Price",
        includeZero: false,
        prefix: "$"
      },
      axisX: {
        title: `${this.state.currentYear} year`,
        interval: 50
      },
      data: [
        {
          type: "line",

          dataPoints: this.getDataPoints()
        }
      ]
    };
    return <CanvasJSChart options={options} />;
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSumbit}>
          <select
            value={this.state.inputValue}
            onChange={this.handleInputChange}
          >
            {companyData["symbolsList"].map((company, index) => {
              return <option key={index}>{company.symbol}</option>;
            })}
          </select>
          <button type="submit">Submit</button>
        </form>
        <select onChange={this.handleChange}>
          <option value="one">one</option>
          <option value="two">two</option>
          <option value="three">three</option>
        </select>
        {this.generateGraph()}
        <div>
          <ul>
            {Object.keys(this.state.currentCompanyInfo).map(data => {
              return (
                <div key={data}>
                  {(this.state.currentCompanyInfo[data] === "True" ||
                    this.state.currentCompanyInfo[data] === "False") && (
                    <li>
                      {data
                        .split(" ")
                        .slice(0, -1)
                        .join(" ")}
                    </li>
                  )}
                  <p>
                    {(this.state.currentCompanyInfo[data] == "True" ||
                      this.state.currentCompanyInfo[data] == "False") &&
                      this.state.currentCompanyInfo[data]}{" "}
                  </p>
                </div>
              );
            })}
          </ul>
        </div>
      </div>
    );
  }
}

export default SearchCompanies;
