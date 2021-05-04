import React, { useState } from "react";
import { Form, Input, Button, Card } from 'antd';


const Bridge = ({ deposit, withdrawl }) => {
    const [form] = Form.useForm();
    const [depAmount, setDepAmount] = useState('');
    const [withdrawlAmount, setWithdrawlAmount] = useState('');

    const layout = {
        labelCol: { span: 8 },
        wrapperCol: { span: 6 },
      };
      const tailLayout = {
        wrapperCol: { offset: 8, span: 6 },
      };

    return (
        <Card className="bridge_card">
            <Form {...layout} form={form} name="control-hooks">
                <Form.Item name="deposit" label="Deposit" >
                    <Input onChange={e => setDepAmount(e.target.value)}/>
                </Form.Item>
                <Form.Item name="withdrawl" label="Withdrawl">
                    <Input onChange={e => setWithdrawlAmount(e.target.value)}/>
                </Form.Item>
                <Form.Item {...tailLayout}>
                        <Button onClick={() => deposit(depAmount)} type="primary" htmlType="submit">
                            Deposit
                        </Button>
                        <Button onClick={() => withdrawl(withdrawlAmount)} type="primary" htmlType="submit">
                            Withdrawl
                        </Button>
                </Form.Item>
            </Form>
        </Card>
    )
}

export default Bridge;