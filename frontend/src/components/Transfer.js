import React, { useState } from "react";
import { Form, Input, Button, Card } from 'antd';
import './Transfer.css';

const Transfer = ({ tokenBalance, tokenName, switchLayer, transfer }) => {
    const [form] = Form.useForm();
    const [to, setTo] = useState('');
    const [amount, setAmount] = useState(0);

    const layout = {
        labelCol: { span: 8 },
        wrapperCol: { span: 6 },
      };
      const tailLayout = {
        wrapperCol: { offset: 8, span: 6 },
      };

    return(
        <div className="container">
            <Card className="transfer_card">
                <h1 style={{ textAlign:"center", size: 4 }}>Balance: {tokenBalance} {tokenName}</h1>
                <Button onClick={() =>switchLayer()}>Switch</Button>
                <Form {...layout} className="form_container" form={form} name="control-hooks">
                    <Form.Item name="to" label="To" rules={[{ required: true }]}>
                        <Input className="input_box" onChange={e => setTo(e.target.value)}/>
                    </Form.Item>

                    <Form.Item name="amount" label="Amount" rules={[{ required: true }]}>
                        <Input className="input_box" onChange={e => setAmount(e.target.value)} />
                    </Form.Item>

                    <Form.Item {...tailLayout}>
                        <Button style={{display:"flex", justifyContent: "center"}} onClick={() => transfer(to, amount)} type="primary" htmlType="submit">
                            Submit
                        </Button>
                    </Form.Item>
                </Form>
            </Card>
        </div>
    );
}


export default Transfer;