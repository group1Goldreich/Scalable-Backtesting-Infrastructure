import React, { useState } from 'react';

function BacktestForm() {
  const [parameters, setParameters] = useState({
    startDate: '',
    endDate: '',
    indicator: '',
    paramsRange: '',
  });

  const handleChange = (e) => {
    setParameters({
      ...parameters,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(parameters);
    // Handle form submission, e.g., send to backend
  };

  return (
    <div className="card bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">Backtest Parameters</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Start Date</span>
            </label>
            <input
              type="date"
              name="startDate"
              value={parameters.startDate}
              onChange={handleChange}
              className="input input-bordered"
              required
            />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">End Date</span>
            </label>
            <input
              type="date"
              name="endDate"
              value={parameters.endDate}
              onChange={handleChange}
              className="input input-bordered"
              required
            />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Technical Indicator</span>
            </label>
            <input
              type="text"
              name="indicator"
              value={parameters.indicator}
              onChange={handleChange}
              className="input input-bordered"
              placeholder="e.g., SMA, EMA"
              required
            />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Indicator Parameters Range</span>
            </label>
            <input
              type="text"
              name="paramsRange"
              value={parameters.paramsRange}
              onChange={handleChange}
              className="input input-bordered"
              placeholder="e.g., 5, 10, 20"
              required
            />
          </div>
          <div className="form-control mt-4">
            <button type="submit" className="btn btn-primary">
              Run Backtest
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default BacktestForm;
